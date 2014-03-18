Summary:	Compositor protocol
Name:		wayland
Version:	1.4.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	332cf9191837be12638a29265ed7cf46
URL:		http://wayland.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	pkgconfig(libffi)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wayland is a project to define a protocol for a compositor to talk to
its clients as well as a library implementation of the protocol. The
compositor can be a standalone display server running on Linux kernel
modesetting and evdev input devices, an X application, or a Wayland
client itself. The clients can be traditional applications, X servers
(rootless or fullscreen) or other display servers.

%package devel
Summary:	Header files for Wayland libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libffi-devel

%description devel
Header files for Wayland libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-documentation	\
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwayland-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%attr(755,root,root) %ghost %{_libdir}/libwayland-client.so.0
%attr(755,root,root) %ghost %{_libdir}/libwayland-cursor.so.0
%attr(755,root,root) %ghost %{_libdir}/libwayland-server.so.0
%attr(755,root,root) %{_libdir}/libwayland-client.so.*.*.*
%attr(755,root,root) %{_libdir}/libwayland-cursor.so.*.*.*
%attr(755,root,root) %{_libdir}/libwayland-server.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wayland-scanner
%attr(755,root,root) %{_libdir}/libwayland*.so
%{_includedir}/wayland-*.h
%{_datadir}/wayland
%{_npkgconfigdir}/*.pc
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/wayland-scanner.m4

