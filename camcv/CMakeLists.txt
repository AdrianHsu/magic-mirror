
cmake_minimum_required(VERSION 2.8)
project( camcv )
SET(COMPILE_DEFINITIONS -Werror)

find_package( OpenCV REQUIRED )
link_directories( /home/pi/bytefish-libfacerec-e1b143d )

set (GL_SCENE_SOURCES
gl_scenes/models.c
gl_scenes/mirror.c
gl_scenes/yuv.c
gl_scenes/sobel.c
gl_scenes/square.c
gl_scenes/teapot.c
gl_scenes/vcsm_square.c)

SET(CMAKE_EXE_LINKER_FLAGS "-lpthread -lm")

include_directories(/opt/vc/include)
include_directories(/opt/vc/include/EGL)
include_directories(/opt/vc/userland-master/host_applications/linux/libs/sm)
include_directories(/opt/vc/userland-master/host_applications/linux/libs/bcm_host/include)
include_directories(/opt/vc/userland-master/host_applications/linux/apps/raspicam/gl_scenes)
include_directories(/opt/vc/userland-master/interface/vcos)
include_directories(/opt/vc/userland-master)
include_directories(/opt/vc/userland-master/interface/vcos)
include_directories(/opt/vc/userland-master/interface/vcos/pthreads)
include_directories(/opt/vc/userland-master/interface/vmcs_host/linux)
include_directories(/home/pi/camcv)

add_executable(camcv RaspiCamControl.c RaspiCLI.c RaspiPreview.c camcv_vid1.cpp
RaspiTex.c RaspiTexUtil.c tga.c ${GL_SCENE_SOURCES})

target_link_libraries(camcv /opt/vc/lib/libmmal_core.so
/opt/vc/lib/libmmal_util.so /opt/vc/lib/libmmal_vc_client.so
/opt/vc/lib/libGLESv2.so /opt/vc/lib/libEGL.so
/opt/vc/lib/libvcos.so /opt/vc/lib/libbcm_host.so
/opt/vc/lib/libvcsm.so libpthread.so /opt/vc/lib/libbrcmEGL.so
/opt/vc/lib/libbrcmGLESv2.so libm.so 
/home/pi/bytefish-libfacerec-e1b143d/libopencv_facerec.a
${OpenCV_LIBS})
