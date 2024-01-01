#! /usr/bin/tclsh 
# Generated for VCF on 2024-01-01 17:50:54.986788
# This task is used to do formal coverage analysis on the design.

set_app_mode FCA

set_app_var fml_reset_property_check true
set_app_var fml_cov_enable_branch_cov true
set_app_var fml_cov_tgl_enable_input_port true
set_app_var fml_cov_override_db_opt true

read_cov_db -cov_input simv.vdb -cov_dut tb.inst

set_blackbox -designs { add.v sub.v }
set_blackbox -cells { add.v sub.v }

report_blackbox

read_file -top adder -covline+cond+tgl+fsm_state+fsm_transition+branch+cg -format verilog -sva -vcs "-f { adder.v adder_tb.v mult.v }" -assert svaext -lca

read_fault_db -name adder.certitude
save_fault_db -name adder.certitude

set_clock -name clk -period 10

check_fv block

