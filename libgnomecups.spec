%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	1
%define libname %mklibname gnomecups %{api} %{major}
%define devname %mklibname gnomecups -d

Summary:	GNOME library for CUPS integration
Name:		libgnomecups
Version:	0.2.3
Release:	14
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnomecups/%{url_ver}/%{name}-%{version}.tar.bz2
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
Patch10:	libgnomecups-0.2.3-automake-1.13.patch
Patch11:	libgnomecups-lpoptions.patch
Patch12:	libgnomecups-0.2.3-cups-1.6.patch

BuildRequires:	cups-common
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)

%description
GNOME library for CUPS integration

%package -n %{libname}
Summary:	GNOME library for CUPS integration
Group:		System/Libraries
Suggests:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}gnomecups-1.0_1 < 0.2.3-11

%description -n %{libname}
GNOME library for CUPS integration

%package -n %{devname}
Summary:	GNOME library for CUPS integration
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gnomecups-1.0-devel < 0.2.3-11

%description -n %{devname}
GNOME library for CUPS integration

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
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

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so

