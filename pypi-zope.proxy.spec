#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.proxy
Version  : 4.5.1
Release  : 60
URL      : https://files.pythonhosted.org/packages/c5/40/5ee2821c4e469e935bc6d2b060f89af00cb40fafd96a34ea0dc3c90771c1/zope.proxy-4.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/40/5ee2821c4e469e935bc6d2b060f89af00cb40fafd96a34ea0dc3c90771c1/zope.proxy-4.5.1.tar.gz
Summary  : Generic Transparent Proxies
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.proxy-filemap = %{version}-%{release}
Requires: pypi-zope.proxy-lib = %{version}-%{release}
Requires: pypi-zope.proxy-license = %{version}-%{release}
Requires: pypi-zope.proxy-python = %{version}-%{release}
Requires: pypi-zope.proxy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.interface)
BuildRequires : python3-dev

%description
================
``zope.proxy``
================
.. image:: https://img.shields.io/pypi/v/zope.proxy.svg
:target: https://pypi.python.org/pypi/zope.proxy/
:alt: Latest Version

%package dev
Summary: dev components for the pypi-zope.proxy package.
Group: Development
Requires: pypi-zope.proxy-lib = %{version}-%{release}
Provides: pypi-zope.proxy-devel = %{version}-%{release}
Requires: pypi-zope.proxy = %{version}-%{release}

%description dev
dev components for the pypi-zope.proxy package.


%package filemap
Summary: filemap components for the pypi-zope.proxy package.
Group: Default

%description filemap
filemap components for the pypi-zope.proxy package.


%package lib
Summary: lib components for the pypi-zope.proxy package.
Group: Libraries
Requires: pypi-zope.proxy-license = %{version}-%{release}
Requires: pypi-zope.proxy-filemap = %{version}-%{release}

%description lib
lib components for the pypi-zope.proxy package.


%package license
Summary: license components for the pypi-zope.proxy package.
Group: Default

%description license
license components for the pypi-zope.proxy package.


%package python
Summary: python components for the pypi-zope.proxy package.
Group: Default
Requires: pypi-zope.proxy-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.proxy package.


%package python3
Summary: python3 components for the pypi-zope.proxy package.
Group: Default
Requires: pypi-zope.proxy-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(zope.proxy)
Requires: pypi(setuptools)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-zope.proxy package.


%prep
%setup -q -n zope.proxy-4.5.1
cd %{_builddir}/zope.proxy-4.5.1
pushd ..
cp -a zope.proxy-4.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663257309
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.proxy
cp %{_builddir}/zope.proxy-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.proxy/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.10/zope.proxy/proxy.h

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-zope.proxy

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.proxy/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
