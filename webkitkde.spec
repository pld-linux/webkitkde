#
# Conditional build:
#
%define		qt_ver		4.4.3
%define		kdever		4.2.0
%define		snap		981623

Summary:	webkitkde
Summary(pl.UTF-8):	webkitkde
Name:		webkitkde
Version:	0
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Libraries
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/libs/webkitkde/
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	ec03b5d4dd9dbb548bc57e8d404c69d8
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtWebKit-devel >= %{qt_ver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebKitKde.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for webkitkde library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki webkitkde
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for webkitkde library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki webkitkde.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdewebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdewebkit.so.?
%attr(755,root,root) %{_libdir}/libwebkitkde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkitkde.so.?
%attr(755,root,root) %{_libdir}/kde4/webkitkdepart.so
%{_datadir}/kde4/services/webkitpart.desktop
%{_datadir}/apps/webkitpart
%{_iconsdir}/*/*/*/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdewebkit.so
%attr(755,root,root) %{_libdir}/libwebkitkde.so
%{_includedir}/KDE/KdeWebKit
%{_includedir}/KDE/WebKitPart
%{_includedir}/kdewebkit
%{_includedir}/webkitkde
%{_datadir}/apps/cmake/modules/*.cmake
