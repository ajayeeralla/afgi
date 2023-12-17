import os


# run tool on a given TCL script
def run_tool(tool, script, args, output_dir, output_file):
    # create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # run tool
    os.system(tool + ' ' + script + ' ' + args + ' > ' + output_dir + '/' + output_file)