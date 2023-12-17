#! /usr/bin/tclsh 
#Generated on 2023-12-15 19:52:08.919177

set_app_mode FPV

read_file -top None -format None -sva -vcs "-f None" -assert svaext -lca

create_clock -name None -period 100

create_reset -name None -sense high

sim_run -stable 
sim_save_reset 

check_fv