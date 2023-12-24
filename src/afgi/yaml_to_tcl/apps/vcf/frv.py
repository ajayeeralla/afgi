from afgi.yaml_to_tcl.apps.vcf.fpv import FPV
class FRV(FPV):
    def frv_load(self):
        ipxact_file = self.dic['ipxact']
        self.output_file.writelines("frv_load -ipxact "+ipxact_file+" -auto_load\n\n")

