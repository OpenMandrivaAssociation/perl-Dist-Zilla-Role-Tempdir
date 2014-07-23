%define upstream_name    Dist-Zilla-Role-Tempdir
%define upstream_version 1.000000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Shell Out and collect the result in a DZ plug-in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::base)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Tempdir)
BuildRequires:	perl(File::chdir)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
Shell Out and collect the result in a DZ plug-in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*
