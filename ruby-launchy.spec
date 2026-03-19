%define pkgname launchy
Summary:	Helper class for launching cross-platform applications
Name:		ruby-%{pkgname}
Version:	3.1.1
Release:	1
License:	ISC
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	fb281c5f82905c6a98ea84696c6a2654
URL:		https://github.com/copiousfreetime/launchy
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	sed >= 4.0
Requires:	ruby-addressable >= 2.8
Requires:	ruby-childprocess >= 5.0
Requires:	ruby-logger >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Launchy is helper class for launching cross-platform applications in a
fire and forget manner.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' exe/launchy

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a exe/launchy $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.md README.md LICENSE.txt
%attr(755,root,root) %{_bindir}/launchy
%{ruby_vendorlibdir}/launchy.rb
%{ruby_vendorlibdir}/launchy
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
