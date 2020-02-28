#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-roboto-fontface
Version  : 0.5.0.0
Release  : 17
URL      : http://pypi.debian.net/XStatic-roboto-fontface/XStatic-roboto-fontface-0.5.0.0.tar.gz
Source0  : http://pypi.debian.net/XStatic-roboto-fontface/XStatic-roboto-fontface-0.5.0.0.tar.gz
Summary  : roboto-fontface 0.5.0 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-roboto-fontface-license = %{version}-%{release}
Requires: XStatic-roboto-fontface-python = %{version}-%{release}
Requires: XStatic-roboto-fontface-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
XStatic-roboto-fontface
-----------------------

roboto-fontface javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by **any** project that needs these files.

It intentionally does **not** provide any extra code except some metadata
**nor** has any extra requirements. You MAY use some minimal support code from
the XStatic base package, if you like.

You can find more info about the xstatic packaging way in the package
`XStatic`.

%package license
Summary: license components for the XStatic-roboto-fontface package.
Group: Default

%description license
license components for the XStatic-roboto-fontface package.


%package python
Summary: python components for the XStatic-roboto-fontface package.
Group: Default
Requires: XStatic-roboto-fontface-python3 = %{version}-%{release}
Provides: xstatic-roboto-fontface-python

%description python
python components for the XStatic-roboto-fontface package.


%package python3
Summary: python3 components for the XStatic-roboto-fontface package.
Group: Default
Requires: python3-core
Provides: pypi(XStatic-roboto-fontface)

%description python3
python3 components for the XStatic-roboto-fontface package.


%prep
%setup -q -n XStatic-roboto-fontface-0.5.0.0
cd %{_builddir}/XStatic-roboto-fontface-0.5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582850300
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/XStatic-roboto-fontface
cp %{_builddir}/XStatic-roboto-fontface-0.5.0.0/xstatic/pkg/roboto_fontface/data/LICENSE %{buildroot}/usr/share/package-licenses/XStatic-roboto-fontface/39644573b71d2ecc99d29f510ffb0ba53fe07b62
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/XStatic-roboto-fontface/39644573b71d2ecc99d29f510ffb0ba53fe07b62

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
