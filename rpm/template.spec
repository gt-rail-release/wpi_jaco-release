Name:           ros-indigo-jaco-teleop
Version:        0.0.23
Release:        0%{?dist}
Summary:        ROS jaco_teleop package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jaco_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-wpi-jaco-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-wpi-jaco-msgs

%description
Various Nodes for Teleoperating the JACO Arm

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon May 04 2015 David Kent <davidkent@wpi.edu> - 0.0.23-0
- Autogenerated by Bloom

* Wed Apr 22 2015 David Kent <davidkent@wpi.edu> - 0.0.22-0
- Autogenerated by Bloom

* Fri Apr 17 2015 David Kent <davidkent@wpi.edu> - 0.0.21-0
- Autogenerated by Bloom

* Tue Apr 14 2015 David Kent <davidkent@wpi.edu> - 0.0.20-0
- Autogenerated by Bloom

* Fri Apr 10 2015 David Kent <davidkent@wpi.edu> - 0.0.19-0
- Autogenerated by Bloom

* Fri Apr 03 2015 David Kent <davidkent@wpi.edu> - 0.0.18-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 0.0.17-0
- Autogenerated by Bloom

* Tue Mar 24 2015 David Kent <davidkent@wpi.edu> - 0.0.16-0
- Autogenerated by Bloom

* Tue Feb 17 2015 David Kent <davidkent@wpi.edu> - 0.0.15-0
- Autogenerated by Bloom

* Fri Feb 06 2015 David Kent <davidkent@wpi.edu> - 0.0.14-0
- Autogenerated by Bloom

* Tue Feb 03 2015 David Kent <davidkent@wpi.edu> - 0.0.13-0
- Autogenerated by Bloom

* Tue Jan 20 2015 David Kent <davidkent@wpi.edu> - 0.0.12-0
- Autogenerated by Bloom

* Thu Dec 18 2014 David Kent <davidkent@wpi.edu> - 0.0.11-0
- Autogenerated by Bloom

* Fri Dec 12 2014 David Kent <davidkent@wpi.edu> - 0.0.10-0
- Autogenerated by Bloom

* Tue Dec 02 2014 David Kent <davidkent@wpi.edu> - 0.0.9-0
- Autogenerated by Bloom

* Wed Oct 22 2014 David Kent <davidkent@wpi.edu> - 0.0.8-0
- Autogenerated by Bloom

* Fri Sep 19 2014 David Kent <davidkent@wpi.edu> - 0.0.7-0
- Autogenerated by Bloom

* Tue Sep 02 2014 David Kent <davidkent@wpi.edu> - 0.0.6-0
- Autogenerated by Bloom

* Mon Aug 25 2014 David Kent <davidkent@wpi.edu> - 0.0.5-0
- Autogenerated by Bloom

