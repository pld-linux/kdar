
# Conditional build:
%bcond_with     verbose # verbose build

Summary:	KDar - K Disk archiver
Summary(pl):	KDar - archiwizer dysków K
Name:		kdar
Version:	1.3.2
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/kdar/%{name}-%{version}.tar.bz2
# Source0-md5:	957a3f196a1966d481c2bcff81a1e0b8
Source1:	%{name}.desktop
URL:		http://kdar.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dar-devel >= 2.1.4-2
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	unsermake >= 040511
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Disk archiver (KDar) is a KDE GUI-based backup and archiving
program. Use it to prepare your data for storage on CD-Rs, jazz
drives, floppies, even DVDs. KDar uses the dar library by Denis
Corbin. Features include compression and archive splitting.

%description -l pl
KDar - archiwizer dysków K jest bazowanym na GUI KDE programem do
tworzenia kopii zapasowych i archiwizacji. Mo¿na go u¿ywaæ do
przygotowania danych maj±cych siê znale¼æ na p³ytach CD-R, napêdach
jazz, dyskietkach, czy nawet DVD. KDar wykorzystuje bibliotekê dar
Denisa Corbina. Pozwala na kompresjê i podzia³ archiwów.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
	--enable-largefile \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make} %{?with_verbose:VERBOSE=1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO USAGE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*
