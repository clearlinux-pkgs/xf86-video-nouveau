#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-video-nouveau
Version  : 1.0.15
Release  : 8
URL      : https://www.x.org/releases/individual/driver/xf86-video-nouveau-1.0.15.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-nouveau-1.0.15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-nouveau-lib
Requires: xf86-video-nouveau-doc
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_nouveau)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
No detailed description available

%package doc
Summary: doc components for the xf86-video-nouveau package.
Group: Documentation

%description doc
doc components for the xf86-video-nouveau package.


%package lib
Summary: lib components for the xf86-video-nouveau package.
Group: Libraries

%description lib
lib components for the xf86-video-nouveau package.


%prep
%setup -q -n xf86-video-nouveau-1.0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507171878
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507171878
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/nouveau_drv.so
