Summary:	Plugins for the Eye of GNOME image viewer
Name:     	eog-plugins
Version:	3.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/projects/eog/
Source0: 	ftp://ftp.gnome.org:21/pub/GNOME/sources/eog-plugins/3.8/%{name}-%{version}.tar.xz

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


%changelog
* Sun May 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 800826
- update to new version 3.4.1

* Tue May 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.0-1
+ Revision: 798926
- BR: GL-devel
- version update 3.4.0

* Wed Mar 14 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2-1
+ Revision: 785011
- new version 3.2.2
- cleaned up spec

  + Götz Waschk <waschk@mandriva.org>
    - rebuild

* Sat Feb 05 2011 Götz Waschk <waschk@mandriva.org> 2.30.2-1
+ Revision: 636218
- new version
- drop patch

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-3mdv2011.0
+ Revision: 574685
- build with new champlain

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-2mdv2011.0
+ Revision: 551159
- useless release bump
- update to new version 2.30.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528948
- update to new version 2.30.0

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509950
- update to new version 2.29.91

* Mon Feb 15 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-3mdv2010.1
+ Revision: 506086
- add missing postasa data files
- update description

* Mon Feb 15 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-2mdv2010.1
+ Revision: 506058
- enable postasa plugin

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 504124
- new version
- update file list

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 490061
- update to new version 2.29.5

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 475378
- new version
- update file list

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458858
- Release 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446729
- new version
- drop patch

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-2mdv2010.0
+ Revision: 441032
- patch for new libchamplain

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437406
- new version
- drop patches

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-3mdv2010.0
+ Revision: 421368
- replace postr filename patch by upstream version
- fix crash in exif view

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-2mdv2010.0
+ Revision: 420887
- fix call to postr
- update description

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420838
- import eog-plugins


