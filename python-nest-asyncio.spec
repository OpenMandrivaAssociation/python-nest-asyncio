Name:		python-nest-asyncio
Version:	1.6.0
Release:	2
Summary:	Patch asyncio to allow nested event loops
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://github.com/erdewit/nest_asyncio
Source0:	https://files.pythonhosted.org/packages/source/n/nest_asyncio/nest_asyncio-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
A small patch that lets asyncio.run() and loop.run_until_complete()
be nested, used by Jupyter, Unsloth and other libraries that already
run inside an event loop.

# Single-module package: drop the top-level __pycache__ so it is
# not left unpackaged (and extra tests stay quiet).
%install -a
rm -rf %{buildroot}%{py_sitedir}/__pycache__

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/nest_asyncio.py
%{py_sitedir}/nest_asyncio-*.*-info
