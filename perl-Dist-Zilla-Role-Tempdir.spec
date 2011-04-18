%define upstream_name    Dist-Zilla-Role-Tempdir
%define upstream_version 0.01027622

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Shell Out and collect the result in a DZ plug-in
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Digest::base)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Tempdir)
BuildRequires: perl(File::chdir)
BuildRequires: perl(Moose)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Module::Build)
BuildRequires: perl(namespace::autoclean)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


