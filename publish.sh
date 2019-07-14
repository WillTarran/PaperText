for files in $@
do
    jupytext --to notebook $files
    file_root=$( echo $files | sed ' s/.py// ' )
    papermill $file_root.ipynb $file_root.report.ipynb -f params.yaml
    jupyter nbconvert --to html $file_root.report.ipynb && rm $file_root.report.ipynb
done
