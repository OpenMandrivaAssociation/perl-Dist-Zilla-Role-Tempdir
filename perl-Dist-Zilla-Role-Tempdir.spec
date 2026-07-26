%define upstream_name    Dist-Zilla-Role-Tempdir
Name:		perl-%{upstream_name}
Version:	1.001003
Release:	2

Summary:	Shell Out and collect the result in a DZ plug-in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/kentnl/Dist-Zilla-Role-Tempdir
Source0:	https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Dist-Zilla-Role-Tempdir-%{version}.tar.gz

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
%setup -q -n %{upstream_name}-%{version}

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


