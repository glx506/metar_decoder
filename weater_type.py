# Weather type
    result = re.search(r'''[\-\+]DZ|RA|\-RA|\+RA|SN|\-SN|\+SN|SG|\-SG
                           |\+SG|PL|\-PL|\+PL|GS|\-GS|\+GS
                           |RASN|\-RASN|\+RASN|SNRA|\-SNRA|\+SNRA
                           |SHSN|\-SHSN|\+SHSN|SHRA|\-SHRA|\+SHRA
                           |SHGR|\-SHGR|\+SHGR|FZRA|\-FZRA|\+FZRA
                           |FZDZ|\-FZDZ|\+FZDZ|TSRA|\-TSRA|\+TSRA
                           |SHGR|\-SHGR|\+SHGR|FZRA|\-FZRA|\+FZRA
                           |TSGR|\-TSGR|\+TSGR|TSGS|\-TSGS|\+TSGS
                           |TSSN|\-TSSN|\+TSSN|DS|\-DS|\+DS|SS|\-SS|\+SS
                           |FG|FZFG|VCFG|MIFG|PRFG|BCFG|BR|HZ|FU|DRSN|DRSA|DRDU
                           |DU|BLSN|BLDU|SQ|IC|TS|VCTS|VA''', metar_data)
