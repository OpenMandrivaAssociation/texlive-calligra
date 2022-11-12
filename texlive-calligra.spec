Name:		texlive-calligra
Version:	15878
Release:	1
Summary:	Calligraphic font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/calligra
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A calligraphic font in the handwriting style of the author,
Peter Vanroose. The font is supplied as MetaFont source LaTeX
support of the font is provided in the calligra package in the
fundus bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/calligra/callig15.mf
%{_texmfdistdir}/fonts/source/public/calligra/calligra.mf
%{_texmfdistdir}/fonts/tfm/public/calligra/callig15.tfm
%doc %{_texmfdistdir}/doc/latex/calligra/README
%doc %{_texmfdistdir}/doc/latex/calligra/testfont.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
