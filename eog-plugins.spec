Summary:	Plugins for the Eye of GNOME image viewer
Name:     	eog-plugins
Version:	3.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/projects/eog/
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:	pkgconfig(champlain-0.12)
#BuildRequires:	pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(eog)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  GL-devel

Requires: eog
Requires: postr

%description
This is the Eye of Gnome, an image viewer program. It is meant
to be a fast and functional image viewer as well as an image
cataloging program. It does proper handling of large images and
images with full opacity information, and can zoom and scroll
images quickly while keeping  memory usage constant.

This package contains additional plugins for EOG:
Map
Exif display
Zoom to fit image width
Flickr Uploader
PicasaWeb Uploader
Python Console
Send By Mail
Slideshow Shuffle

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/eog/plugins/*.la

%{find_lang} %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_datadir}/eog/plugins/*
%{_libdir}/eog/plugins/*
%{_datadir}/glib-2.0/schemas/*.xml
