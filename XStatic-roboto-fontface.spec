#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-roboto-fontface
Version  : 0.4.3.2
Release  : 7
URL      : https://pypi.python.org/packages/source/X/XStatic-roboto-fontface/XStatic-roboto-fontface-0.4.3.2.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-roboto-fontface/XStatic-roboto-fontface-0.4.3.2.tar.gz
Summary  : roboto-fontface 0.4.3 (XStatic packaging standard)
Group    : Development/Tools
License  : Apache-2.0
Requires: XStatic-roboto-fontface-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-roboto-fontface
-----------------------
roboto-fontface javascript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-roboto-fontface package.
Group: Default
Provides: xstatic-roboto-fontface-python

%description python
python components for the XStatic-roboto-fontface package.


%prep
%setup -q -n XStatic-roboto-fontface-0.4.3.2

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
