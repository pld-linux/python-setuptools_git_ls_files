#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Use git to list all files, including submodules
Summary(pl.UTF-8):	Użycie gita do listy wszystkich plików, wraz z podmodułami
Name:		python-setuptools_git_ls_files
Version:	0.1.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools-git-ls-files/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools-git-ls-files/setuptools_git_ls_files-%{version}.tar.gz
# Source0-md5:	4a904dc4b154bff7de3cb41fca67b234
URL:		https://pypi.org/project/setuptools-git-ls-files/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin for setuptools that finds all git tracked files, including
submodules.

%description -l pl.UTF-8
Wtyczka setuptools znajdująca wszystkie pliki śledzone przez gita,
wraz z podmodułami.

%package -n python3-setuptools_git_ls_files
Summary:	Use git to list all files, including submodules
Summary(pl.UTF-8):	Użycie gita do listy wszystkich plików, wraz z podmodułami
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-setuptools_git_ls_files
A plugin for setuptools that finds all git tracked files, including
submodules.

%description -n python3-setuptools_git_ls_files -l pl.UTF-8
Wtyczka setuptools znajdująca wszystkie pliki śledzone przez gita,
wraz z podmodułami.

%prep
%setup -q -n setuptools_git_ls_files-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/setuptools_git_ls_files.py[co]
%{py_sitescriptdir}/setuptools_git_ls_files-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-setuptools_git_ls_files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/setuptools_git_ls_files.py
%{py3_sitescriptdir}/__pycache__/setuptools_git_ls_files.cpython-*.py[co]
%{py3_sitescriptdir}/setuptools_git_ls_files-%{version}-py*.egg-info
%endif
