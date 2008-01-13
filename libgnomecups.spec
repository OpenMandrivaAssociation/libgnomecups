%define name libgnomecups
%define version 0.2.2
%define release %mkrel 5

%define api_version 1.0
%define major 1
%define libname %mklibname gnomecups-%{api_version}_ %{major}
%define develname %mklibname gnomecups-%{api_version} -d

Summary: GNOME library for CUPS integration
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL
Group: System/Libraries
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.2.2-4mdv fix printer detection and cups 1.2 support (SUSE)
Patch0: libgnomecups-0.2.2-cups12.patch
# (fc) 0.2.2-4mdv fix cups callback for authentication (SUSE)
Patch1: libgnomecups-0.2.2-callbackfix.patch
# (fc) 0.2.2-4mdv fix invalid mem access (SVN)
Patch2: libgnomecups-0.2.2-gfree.patch
# (fc) 0.2.2-4mdv add dbus support (Fedora)
Patch3: libgnomecups-0.2.2-dbus.patch
# (fc) 0.2.2-4mdv parse cups loptions (ubuntu)
Patch4: libgnomecups-0.2.2-parse-dot-cups-loptions.patch
# (fc) 0.2.2-4mdv fix remote printer detection (ubuntu)
Patch5: libgnomecups-0.2.2-fix-islocal.patch
# (fc) 0.2.2-4mdv don't warn on stderr for IPP_NOT_FOUND (ubuntu)
Patch6: libgnomecups-0.2.2-ignore-ipp-not-found.patch
# (fc) 0.2.2-4mdv allow to change some cups printer attributes (ubuntu)
Patch7: libgnomecups-0.2.2-replace-set-printer-attrs.patch
BuildRequires: cups-devel cups-common
BuildRequires: glib2-devel
BuildRequires: perl-XML-Parser
BuildRequires: dbus-glib-devel
BuildRequires: intltool
BuildRequires: gnome-common
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GNOME library for CUPS integration

%package -n %{libname}
Summary: GNOME library for CUPS integration
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n %{libname}
GNOME library for CUPS integration

%package -n %{develname}
Summary: GNOME library for CUPS integration
Group: Development/GNOME and GTK+
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-%{api_version}-devel = %{version}-%{release}
Obsoletes: %{mklibname gnomecups-%{api_version}_ 1 -d}

%description -n %{develname}
GNOME library for CUPS integration

%prep
%setup -q
%patch0 -p1 -b .cups12
%patch1 -p1 -b .callbackfix
%patch2 -p1 -b .gfree
%patch3 -p1 -b .dbus
%patch4 -p1 -b .parse-dot-cups-loptions
%patch5 -p1 -b .fix-is-local
%patch6 -p1 -b .ignore-ipp-not-found
%patch7 -p1 -b .replace-set-printer-attrs

#needed by patch3
autoreconf

%build

%configure2_5x --with-dbus=yes

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{libname}

%postun -p /sbin/ldconfig -n %{libname}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog NEWS AUTHORS

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
