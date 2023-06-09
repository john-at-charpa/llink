%define prefix  /usr/local
%define name    libdvdread
%define ver     4.2.0
%define rel     0

Name:           %{name}
Summary:        Low level DVD access library
Version:        %{ver}
Release:        %{rel}
Group:          Development/Libraries
Copyright:      GPL
Url:            http://dvd.sourceforge.net/
Source:         %{name}-%{version}.tar.gz
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libdvdread provides support to applications wishing to make use of basic
DVD reading features.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install-strip DESTDIR=$RPM_BUILD_ROOT

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README
%{prefix}/bin/dvdread-config
%{prefix}/lib/libdvdread*.la
%{prefix}/lib/libdvdread*.so.*
%{prefix}/lib/libdvdread*.so
%{prefix}/include/libdvdread/*
@INSTALL_M4_TRUE@@ACLOCAL_DIR@/dvdread.m4

%changelog
* Sun Mar 18 2002 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- Add missing files. Fix rpm generation.
* Tue Mar 12 2002 Rich Wareham <richwareham@users.sourceforge.net>
- Canabalisation to form libdvdnav spec file.
* Sun Sep 09 2001 Thomas Vander Stichele <thomas@apestaart.org>
- first spec file
