%include	/usr/lib/rpm/macros.perl
Summary:	Extract and convert bitmaps from Windows icon and cursor files
Summary(pl):	Narzêdzie wyci±gaj±ce i konwertuj±ce bitmapy z windowsowych plików ikon i kursorów
Name:		icoutils
Version:	0.22.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
# Source0-md5:	473fdfb30aae3961f7d0da62fbbdf6d7
Patch0:		%{name}-am_fixes.patch
URL:		http://www.student.lu.se/~nbi98oli/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	perl-libwww
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be embedded
in executables and libraries (.dll-files). (Such embedded files are
referred to as resources.)

%description -l pl
icoutils to zestaw programów do wyci±gania i konwertowania bitmap z
plików ikon i kursorów u¿ywanych w Microsoft Windows. Te pliki maj±
zazwyczaj rozszerzenie .ico lub .cur, ale mog± byæ wbudowane w pliki
wykonywalne lub biblioteki (pliki .dll) (takie wbudowane pliki s±
nazywane zasobami).

%prep
%setup  -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
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
