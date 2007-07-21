%define api_version 1.0
%define lib_name %mklibname gnomecups-%{api_version}_ %{lib_major}
%define lib_major 1

Summary: GNOME library for CUPS integration
Name: libgnomecups
Version: 0.2.2
Release: %mkrel 3
License: LGPL
Group: System/Libraries
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: cups-devel cups-common
BuildRequires: glib2-devel
BuildRequires: perl-XML-Parser
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GNOME library for CUPS integration

%package -n %{lib_name}
Summary: GNOME library for CUPS integration
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n %{lib_name}
GNOME library for CUPS integration

%package -n %{lib_name}-devel
Summary: GNOME library for CUPS integration
Group: Development/GNOME and GTK+
Requires: %{lib_name} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-%{api_version}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
GNOME library for CUPS integration

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{lib_name}

%postun -p /sbin/ldconfig -n %{lib_name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog NEWS AUTHORS

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
