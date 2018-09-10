Summary: Universal Boot Loader for embedded devices
Name: u-boot-fslc
Version: v2016.07+git0+e6b42411ab
Release: r0
License: GPLv2+
Group: bootloaders
Packager: Poky <poky@yoctoproject.org>
URL: http://www.denx.de/wiki/U-Boot/WebHome
BuildRequires: virtual/arm-poky-linux-gnueabi-compilerlibs
BuildRequires: openssl-native
BuildRequires: virtual/libc
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc

%description
U-Boot based on mainline U-Boot used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
submitted for revision and it takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n u-boot-fslc-dbg
Summary: Universal Boot Loader for embedded devices - Debugging files
Group: devel

%description -n u-boot-fslc-dbg
U-Boot based on mainline U-Boot used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
submitted for revision and it takes some time to become part of a stable
version, or because it is not applicable for upstreaming.  This package
contains ELF symbols and related sources for debugging purposes.

%package -n u-boot-fslc-staticdev
Summary: Universal Boot Loader for embedded devices - Development files (Static Libraries)
Group: devel
Requires: u-boot-fslc-dev = v2016.07+git0+e6b42411ab-r0

%description -n u-boot-fslc-staticdev
U-Boot based on mainline U-Boot used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
submitted for revision and it takes some time to become part of a stable
version, or because it is not applicable for upstreaming.  This package
contains static libraries for software development.

%package -n u-boot-fslc-dev
Summary: Universal Boot Loader for embedded devices - Development files
Group: devel
Requires: u-boot-fslc = v2016.07+git0+e6b42411ab-r0

%description -n u-boot-fslc-dev
U-Boot based on mainline U-Boot used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
submitted for revision and it takes some time to become part of a stable
version, or because it is not applicable for upstreaming.  This package
contains symbolic links, header files, and related items necessary for
software development.

%package -n u-boot-fslc-doc
Summary: Universal Boot Loader for embedded devices - Documentation files
Group: doc

%description -n u-boot-fslc-doc
U-Boot based on mainline U-Boot used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
submitted for revision and it takes some time to become part of a stable
version, or because it is not applicable for upstreaming.  This package
contains documentation.

%package -n u-boot-fslc-locale
Summary: Universal Boot Loader for embedded devices
Group: bootloaders

%description -n u-boot-fslc-locale
U-Boot based on mainline U-Boot used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
submitted for revision and it takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%files
%defattr(-,-,-,-)
%dir "/boot"
"/boot/u-boot-sd-v2016.07+gitAUTOINC+e6b42411ab-r0.imx"
"/boot/u-boot.imx-sd"
"/boot/u-boot.imx"

%files -n u-boot-fslc-dbg
%defattr(-,-,-,-)

%files -n u-boot-fslc-dev
%defattr(-,-,-,-)

