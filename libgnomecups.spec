%define name libgnomecups
%define version 0.2.2
%define release %mkrel 3

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
BuildRequires: cups-devel cups-common
BuildRequires: glib2-devel
BuildRequires: perl-XML-Parser
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

%build

%configure2_5x

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
