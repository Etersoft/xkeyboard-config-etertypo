Name: typo
Version: 1.0
Release: alt4

Summary: Typographic layout for X11
License: GPL
Group: System/X11

Url: http://regolit.com/2006/11/26/xkb-unicode/

Packager: Devaev Maxim <mdevaev@etersoft.ru>

# http://git.etersoft.ru/people/mdevaev/packages/typo.git
Source: %name-%version.tar

BuildArchitectures: noarch
BuildRequires: rpm-build-compat

%description
Typographic layout for X11

%prep
%setup

%install
mkdir -p %buildroot%_datadir/X11/xkb/symbols
mkdir -p %buildroot%_docdir/typo
cp -f typo/symbols_typo %buildroot%_datadir/X11/xkb/symbols/etertypo
cp -f typo/README %buildroot%_docdir/typo
cp -f typo/xkb-typo-scheme.png %buildroot%_docdir/typo

%files
%_datadir/X11/xkb/symbols/etertypo
%_docdir/typo/*

%changelog
* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt4
- Renamed typo to etertypo

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt3
- Scheme file not replaced at updates

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt2
- Added README text

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt1
- Initial build

