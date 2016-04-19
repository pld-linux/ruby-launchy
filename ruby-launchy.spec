#
# Conditional build:
%bcond_with	tests		# build without tests

%define pkgname launchy
Summary:	Helper class for cross-platform launching of applications
Name:		ruby-%{pkgname}
Version:	0.4.0
Release:	2
License:	BSD
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	951dc54983c29dde427748ce11189d8b
URL:		http://copiousfreetime.rubyforge.org/launchy/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	rubygem(rspec)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Launchy is helper class for launching cross-platform applications in a
fire and forget manner. There are application concepts (browser, email
client, etc) that are common across all platforms, and they may be
launched differently on each platform. Launchy is here to make a
common approach to launching external application from within ruby
programs.

%prep
%setup -q -n %{pkgname}-%{version}

chmod a+rx bin/*
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*


%build
# write .gemspec
%__gem_helper spec

# bogus dep
# s.add_runtime_dependency(%q<rake>, [">= 0.8.1"])
%{__sed} -i -e '/s.add_runtime_dependency.*rake/d' *.gemspec

%if %{with tests}
rspec spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY LICENSE
%attr(755,root,root) %{_bindir}/launchy
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
