Summary:	Plugins for the Eye of GNOME image viewer
Name:		eog-plugins
Version:	3.26.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/projects/eog/
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/eog-plugins/3.8/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(eog)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgdata)

Requires:	eog >= 3.28.4
Requires:	postr

%description
This is the Eye of Gnome, an image viewer program. It is meant
to be a fast and functional image viewer as well as an image
cataloging program. It does proper handling of large images and
images with full opacity information, and can zoom and scroll
images quickly while keeping  memory usage constant.

This package contains additional plugins for EOG:
- Map
- Exif display
- Zoom to fit image width
- Flickr Uploader
- PicasaWeb Uploader
- Python Console
- Send By Mail
- Slideshow Shuffle

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_datadir}/eog/plugins/*
%{_libdir}/eog/plugins/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}//appdata/eog-*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure

%make_build

%install
%make_install

%find_lang %{name} --with-gnome

