# itop_uboot_v2016_09
mx6q/dl/s/spl itop u-boot v2016.09 
 
# Download repository
    git clone https://github.com/eku2013/u-boot-imx6q-itop.git
    cd itop_uboot_v2016_09
 
# Install cross compiler
    apt-get install gcc-arm-linux-gnueabihf
 
# Setup cross compiler
    export CROSS_COMPILE=arm-linux-gnueabihf-
    export ARCH=arm
 
# Build (imx6q)
    make distclean
    make mx6qitop_config
    make
    cp u-boot.imx /tftp/uboot-mx6qitop.imx
 
# Build (imx6dl)
    TODO
 
# Build (imx6s)
    TODO
