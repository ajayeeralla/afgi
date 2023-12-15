from translator.translate_to_vcf_tcl import translate as trans_vcf_tcl
from translator.translate_to_jg_tcl import translate as trans_jg_tcl

def translate(dic):
        tool = dic['tool']['value'] 
        if tool == None:
            tool = dic['tool']['default'] 
        del dic['tool']
        if tool == 'VC-Formal':
            return trans_vcf_tcl(dic)
        elif tool == 'JasperGold':
            return trans_jg_tcl(dic)
        else: 
            return "The tool is not recognized!"