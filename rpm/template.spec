Name:           ros-indigo-jaco-sdk
Version:        0.0.13
Release:        0%{?dist}
Summary:        ROS jaco_sdk package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jaco_sdk
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
BuildRequires:  libusbx
BuildRequires:  ros-indigo-catkin

%description
JACO Software SDK and API

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

