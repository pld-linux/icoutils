%include	/usr/lib/rpm/macros.perl
Summary:	Extract and convert bitmaps from Windows icon and cursor files
Summary(pl):	Narz�dzie wyci�gaj�ce i konwertuj�ce bitmapy z windowsowych plik�w ikon i kursor�w
Name:		icoutils
Version:	0.26.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://savannah.nongnu.org/download/icoutils/%{name}-%{version}.tar.gz
# Source0-md5:	5494ee42a9dad562b49c6b8721f973e8
URL:		http://www.nongnu.org/icoutils/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.5
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be embedded
in executables and libraries (.dll-files). (Such embedded files are
referred to as resources.)

%description -l pl
icoutils to zestaw program�w do wyci�gania i konwertowania bitmap z
plik�w ikon i kursor�w u�ywanych w Microsoft Windows. Te pliki maj�
zazwyczaj rozszerzenie .ico lub .cur, ale mog� by� wbudowane w pliki
wykonywalne lub biblioteki (pliki .dll) (takie wbudowane pliki s�
nazywane zasobami).

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
