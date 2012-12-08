%define api 1.0
%define major 1
%define libname %mklibname gnomecups-%{api}_ %{major}
%define develname %mklibname gnomecups-%{api} -d

Summary:	GNOME library for CUPS integration
Name:		libgnomecups
Version:	0.2.3
Release:	9
License:	LGPL
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.2.2-4mdv fix cups callback for authentication (SUSE)
Patch1:		libgnomecups-0.2.2-callbackfix.patch
# (fc) 0.2.2-4mdv add dbus support (Fedora)
Patch3:		libgnomecups-0.2.3-dbus.patch
# (fc) 0.2.2-4mdv parse cups loptions (ubuntu)
Patch4:		libgnomecups-0.2.2-parse-dot-cups-loptions.patch
# (fc) 0.2.2-4mdv fix remote printer detection (ubuntu)
Patch5:		libgnomecups-0.2.2-fix-islocal.patch
# (fc) 0.2.2-4mdv don't warn on stderr for IPP_NOT_FOUND (ubuntu)
Patch6:		libgnomecups-0.2.2-ignore-ipp-not-found.patch
# (fc) 0.2.2-4mdv allow to change some cups printer attributes (ubuntu)
Patch7:		libgnomecups-0.2.2-replace-set-printer-attrs.patch
Patch8:		libgnomecups-0.2.3-fix-str-fmt.patch
# glib2.0  2.31.x compat patch
Patch9:		libgnomecups-0.2.3_glib_h.patch

BuildRequires:	cups-devel
BuildRequires:	cups-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	intltool
BuildRequires:	gnome-common

%description
GNOME library for CUPS integration

%package -n %{libname}
Summary:	GNOME library for CUPS integration
Group:		System/Libraries
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
GNOME library for CUPS integration

%package -n %{develname}
Summary:	GNOME library for CUPS integration
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname gnomecups-1.0_ 1 -d} < 0.2.3-9

%description -n %{develname}
GNOME library for CUPS integration

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--with-dbus=yes

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog NEWS AUTHORS

%files -n %{libname}
%{_libdir}/libgnomecups-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.2.3-8
+ Revision: 744879
- final adjustment to glib20 patch
- more to added to glib20 patch
- rebuild
- added p9 to fix builds with glib20 2.31.x
- made p8 patch level 1
- employeed apply_patches
- cleaned up spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-7
+ Revision: 661467
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-6mdv2011.0
+ Revision: 602554
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-5mdv2010.1
+ Revision: 518852
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.3-4mdv2010.0
+ Revision: 425554
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.2.3-3mdv2009.1
+ Revision: 364611
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-2mdv2009.0
+ Revision: 222691
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.3-1mdv2008.1
+ Revision: 159226
- new version
- drop patches 0,2
- update patch 3

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.2.2-5mdv2008.1
+ Revision: 150616
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 12 2007 Frederic Crozat <fcrozat@mandriva.com> 0.2.2-4mdv2008.0
+ Revision: 84719
- Fix Buildrequires
-Patch0 (SUSE): fix printer detection and cups 1.2 support
-Patch1 (SUSE): fix cups callback for authentication
-Patch2 (SVN): fix invalid mem access
-Patch3 (Fedora): add dbus support
-Patch4 (Ubuntu): parse cups loptions
-Patch5 (Ubuntu): fix remote printer detection
-Patch6 (Ubuntu): don't warn on stderr for IPP_NOT_FOUND
-Patch7 (Ubuntu): allow to change some cups printer attributes (ubuntu)

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.2-3mdv2008.0
+ Revision: 54167
- rebuild for 2008
- new devel policy
- Import libgnomecups




* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 0.2.2-3mdv2007.0
- fix buildrequires

* Fri Dec 02 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-2mdk
- rebuild for openssl-0.9.8a

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 0.2.2-1mdk
- Release 0.2.2

* Tue Mar  8 2005 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-1mdk
- drop merged patches
- New release 0.2.0

* Tue Dec 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.14-1mdk
- New release 0.1.14

* Tue Nov 23 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.13-2mdk 
- Patch0 (Fedora): asynchronous ppd fetching 
- Patch1 (Fedora): fix deadlock in mainloop

* Tue Oct  5 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.13-1mdk
- New release 0.1.13

* Tue Sep 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.12-1mdk
- New release 0.1.12

* Tue Aug 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.11-1mdk
- New release 0.1.11

* Wed Aug 18 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.10-1mdk
- Release 0.1.10 

* Tue Jul 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.9-2mdk
- fix buildrequires

* Mon Jul 26 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.9-1mdk
- Release 0.1.9 

* Tue Jun  8 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.8-1mdk
- New release 0.1.8

* Wed Aug  6 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 0.1.6-1mdk
- Release 0.1.6

* Thu Jul 17 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 0.1.5-1mdk
- First Mandrake package
