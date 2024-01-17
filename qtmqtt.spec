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
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
QtMqtt module

%package devel
Summary: Development files for %{name}
%description devel
%{summary}

%package examples
Summary: Programming examples for %{name}
%description examples
%{summary}

%prep
%autosetup

%build
%cmake_qt6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Mqtt.so.6*

%files devel
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMqttTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Mqtt/*.cmake
%{_qt6_libdir}/libQt6Mqtt.prl
%{_qt6_libdir}/libQt6Mqtt.so
%{_qt6_libdir}/pkgconfig/Qt6Mqtt.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_headerdir}/QtMqtt/*
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%dir %{_qt6_libdir}/cmake/Qt6Mqtt/
%dir %{_qt6_headerdir}/QtMqtt

%files examples
%{_qt6_examplesdir}

%changelog
* Wed Jan 17 2024 Dana Elfassy <delfassy@redhat.com>
- updated to cmake_qt6
* Wed Jan 17 2024 Dana Elfassy <delfassy@redhat.com>
- edit subpackages description and summary, files and buildrequires condition
* Tue Jan 16 2024 Dana Elfassy <delfassy@redhat.com>
- split to examples subpackage
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
