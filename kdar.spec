Summary:	KDar - K Disk archiver
Summary(pl):	KDar - archiwizer dysków K
Name:		kdar
Version:	2.0.5
Release:	0.1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/kdar/%{name}-%{version}.tar.bz2
# Source0-md5:	56895417aedeb8f4d4de9be7fe9753b2	
Source1:	%{name}.desktop
URL:		http://kdar.sf.net/
BuildRequires:	dar-devel >= 2.2.1
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.3
BuildRequires:	rpmbuild(macros) >= 1.167
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
export CXXFLAGS="%{rpmcxxflags} -DQT_NO_STL"
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--enable-mode=64 \
	--enable-largefile \
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
%{_iconsdir}/hicolor/*/*/*
