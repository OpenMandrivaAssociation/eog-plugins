Summary:	Plugins for the Eye of GNOME image viewer
Name:     	eog-plugins
Version: 2.29.5
Release: %mkrel 1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/projects/eog/

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  eog-devel >= 2.19.0
BuildRequires:  pygtk2.0-devel
BuildRequires:  gnome-python-devel
BuildRequires:  libchamplain-devel
BuildRequires:  libexif-devel
BuildRequires:  postr
BuildRequires:  intltool >= 0.40.0
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
Python Console
Slideshow Shuffle

%prep
%setup -q

%build

%configure2_5x

%make


%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

%{find_lang} %{name} --with-gnome

rm -rf %buildroot%_libdir/eog/plugins/*a 

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS NEWS README
%_libdir/eog/plugins/champlain.eog-plugin
%_libdir/eog/plugins/exif-display.eog-plugin
%_libdir/eog/plugins/fit-to-width.eog-plugin
%_libdir/eog/plugins/postr.eog-plugin
%_libdir/eog/plugins/pythonconsole.eog-plugin
%_libdir/eog/plugins/send-by-mail.eog-plugin
%_libdir/eog/plugins/slideshowshuffle.eog-plugin
%_libdir/eog/plugins/exif-display/
%_libdir/eog/plugins/*.so*
%_libdir/eog/plugins/*.py*
