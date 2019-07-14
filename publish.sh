for files in $1
do
    jupytext --to notebook $files
    file_root=$( echo $files | sed ' s/.py// ' )
    papermill $file_root.ipynb $file_root.new.ipynb -f params.yaml
    jupyter nbconvert --to html $file_root.new.ipynb && rm $file_root.new.ipynb
done
