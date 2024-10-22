import os
import argparse
import toml



def edit_toml(data_dir,toml_file="/home/ywt/lab/lora-scripts/a31_char_new.toml",pretrained_model_name_or_path="/home/ywt/lab/stable-diffusion-webui/models/Stable-diffusion/noob7.safetensors",end="_noob7"):
    with open (toml_file, "r") as f:
        config = toml.load(f)
        
        config["Basics"]["train_data_dir"]=data_dir
        config["Save"]["output_name"]=os.path.basename(data_dir)+end
        config["Basics"]["pretrained_model_name_or_path"]=pretrained_model_name_or_path
        
    with open(toml_file, "w") as f:
        toml.dump(config, f)
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--toml_file', type=str,default="/home/ywt/lab/lora-scripts/a31_char_new.toml", help='config路径')
    parser.add_argument('--data_dir', type=str, help='数据集路径')
    parser.add_argument('--pretrained_model_name_or_path', default="/home/ywt/lab/stable-diffusion-webui/models/Stable-diffusion/noob7.safetensors",type=str, help='预训练模型路径')
    parser.add_argument('--end', type=str,default="_noob7", help='输出模型后缀')
    
    args = parser.parse_args()

    toml_file = args.toml_file
    data_dir = args.data_dir    
    end = args.end
    pretrained_model_name_or_path = args.pretrained_model_name_or_path
    
    edit_toml(data_dir,toml_file,pretrained_model_name_or_path,end)
