%define api 1.0
%define major 1
%define libname %mklibname gnomecups-%{api}_ %{major}
%define develname %mklibname gnomecups-%{api} -d

Summary: GNOME library for CUPS integration
Name: libgnomecups
Version: 0.2.3
Release: 8
License: LGPL
Group: System/Libraries
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.2.2-4mdv fix cups callback for authentication (SUSE)
Patch1: libgnomecups-0.2.2-callbackfix.patch
# (fc) 0.2.2-4mdv add dbus support (Fedora)
Patch3: libgnomecups-0.2.3-dbus.patch
# (fc) 0.2.2-4mdv parse cups loptions (ubuntu)
Patch4: libgnomecups-0.2.2-parse-dot-cups-loptions.patch
# (fc) 0.2.2-4mdv fix remote printer detection (ubuntu)
Patch5: libgnomecups-0.2.2-fix-islocal.patch
# (fc) 0.2.2-4mdv don't warn on stderr for IPP_NOT_FOUND (ubuntu)
Patch6: libgnomecups-0.2.2-ignore-ipp-not-found.patch
# (fc) 0.2.2-4mdv allow to change some cups printer attributes (ubuntu)
Patch7: libgnomecups-0.2.2-replace-set-printer-attrs.patch
Patch8: libgnomecups-0.2.3-fix-str-fmt.patch
# glib2.0  2.31.x compat patch
Patch9:	libgnomecups-0.2.3_glib_h.patch

BuildRequires: cups-devel
BuildRequires: cups-common
BuildRequires: glib2-devel
BuildRequires: perl-XML-Parser
BuildRequires: dbus-glib-devel
BuildRequires: intltool
BuildRequires: gnome-common

%description
GNOME library for CUPS integration

%package -n %{libname}
Summary: GNOME library for CUPS integration
Group: System/Libraries
Suggests: %{name} = %{version}-%{release}

%description -n %{libname}
GNOME library for CUPS integration

%package -n %{develname}
Summary: GNOME library for CUPS integration
Group: Development/GNOME and GTK+
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname gnomecups-%{api}_ 1 -d}

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
rm -rf %{buildroot}

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
