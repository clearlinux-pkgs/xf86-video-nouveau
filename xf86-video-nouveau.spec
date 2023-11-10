#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB178BE4EA075DE07 (imirkin@alum.mit.edu)
#
Name     : xf86-video-nouveau
Version  : 1.0.17
Release  : 541
URL      : https://www.x.org/releases/individual/driver/xf86-video-nouveau-1.0.17.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-nouveau-1.0.17.tar.gz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-nouveau-1.0.17.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-nouveau-lib = %{version}-%{release}
Requires: xf86-video-nouveau-license = %{version}-%{release}
Requires: xf86-video-nouveau-man = %{version}-%{release}
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_nouveau)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
Patch1: 0001-nouveau-fixup-driver-for-new-X-server-ABI.patch
Patch2: 0002-remove-sarea.h-usage.patch

%description
No detailed description available

%package lib
Summary: lib components for the xf86-video-nouveau package.
Group: Libraries
Requires: xf86-video-nouveau-license = %{version}-%{release}

%description lib
lib components for the xf86-video-nouveau package.


%package license
Summary: license components for the xf86-video-nouveau package.
Group: Default

%description license
license components for the xf86-video-nouveau package.


%package man
Summary: man components for the xf86-video-nouveau package.
Group: Default

%description man
man components for the xf86-video-nouveau package.


%prep
%setup -q -n xf86-video-nouveau-1.0.17
cd %{_builddir}/xf86-video-nouveau-1.0.17
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637260449
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1637260449
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-nouveau
cp %{_builddir}/xf86-video-nouveau-1.0.17/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-nouveau/b6e9e05950ebcd16852fe9795b564a3f5d976223
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/nouveau_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-nouveau/b6e9e05950ebcd16852fe9795b564a3f5d976223

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/nouveau.4
