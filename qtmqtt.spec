%global qt_module qtmqtt

Name:           %{qt_module}
Version:        6.6.0
Release:        1%{?dist}
Summary:        Qt6 - Mqtt module

License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://github.com/qt/qtmqtt
Source0:        qtmqtt-6.6.0.tar.gz

BuildRequires:  cmake >= 3.16 
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtbase-private-devel

%description
QtMqtt module

%package devel
Summary: qt6-qtmqtt-devel subpackage
%description devel

%prep
%autosetup

%build
%cmake_qt6 -DQT_BUILD_EXAMPLES:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%doc tests/README.txt
%{_qt6_libdir}/libQt6Mqtt.so.6*

%files devel
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMqttTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Mqtt/*.cmake
%{_qt6_libdir}/libQt6Mqtt.prl
%{_qt6_libdir}/libQt6Mqtt.so
%{_qt6_libdir}/pkgconfig/Qt6Mqtt.pc
%{_includedir}/qt6
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%dir %{_qt6_libdir}/cmake/Qt6Mqtt/


%changelog
* Tue Jan 16 2024 Dana Elfassy <delfassy@redhat.com>
- fixed devel package name
* Tue Jan 16 2024 Dana Elfassy <delfassy@redhat.com>
- split to -devel subpackage (examples disables)
* Tue Jan 16 2024 Dana Elfassy <delfassy@redhat.com>
- Disable examples
* Tue Jan 16 2024 Dana Elfassy <delfassy@redhat.com>
- Mqtt added BuildRequires and files #2
* Sun Jan 14 2024 Dana Elfassy <delfassy@redhat.com>
- Mqtt added BuildRequires and files
* Thu Jan 11 2024 Dana Elfassy <delfassy@redhat.com>
- Mqtt initial release
