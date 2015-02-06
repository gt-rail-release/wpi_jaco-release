Name:           ros-indigo-wpi-jaco
Version:        0.0.14
Release:        0%{?dist}
Summary:        ROS wpi_jaco package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/wpi_jaco
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-jaco-description
Requires:       ros-indigo-jaco-interaction
Requires:       ros-indigo-jaco-sdk
Requires:       ros-indigo-jaco-teleop
Requires:       ros-indigo-wpi-jaco-msgs
Requires:       ros-indigo-wpi-jaco-wrapper
BuildRequires:  ros-indigo-catkin

%description
Metapackage for the ROS Packages for the JACO Arm Developed at WPI

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
* Fri Feb 06 2015 David Kent <davidkent@wpi.edu> - 0.0.14-0
- Autogenerated by Bloom

* Tue Feb 03 2015 David Kent <davidkent@wpi.edu> - 0.0.13-0
- Autogenerated by Bloom

* Tue Jan 20 2015 David Kent <davidkent@wpi.edu> - 0.0.12-0
- Autogenerated by Bloom

* Thu Dec 18 2014 David Kent <davidkent@wpi.edu> - 0.0.11-0
- Autogenerated by Bloom

