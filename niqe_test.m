cu_niqe = 0;
cu_bli = 0;
cu_sseq = 0;

%sseq_path = '/data/CYQ/190119_CompBuliding/AcquisitionMultipleCamera-18274488-0.bmp';
%sseq_img = imread(sseq_path);
%cu_sseq = SSEQ(sseq_img);

img_path = '/home/luohuixiang/RaindropRemoval/attentive-gan-derainnet/TF_res/test_a_15conn/';
%img_path = '/home/luohuixiang/RaindropRemoval/DeRaindrop/demo/output/'
ext = '*.png';
dis = dir([img_path ext]);
nms = {dis.name};
for k = 1:1:length(nms)
    nm = [img_path nms{k}]
    I = imread(nm);
    niqeI = niqe(I);
    %sseqI = SSEQ(I);
    %blI = bliinds2.bliinds2_score(I);
    cu_niqe = cu_niqe+niqeI;
    %cu_sseq = sseqI+cu_sseq;
    %cu_bli = blI+cu_bli;
end
fprintf('NIQE score is %0.4f.\n',cu_niqe/length(nms))
%fprintf('SSEQ score is %0.4f.\n',cu_sseq/length(nms))
%fprintf('BLIINDS-II score is %0.4f.\n',cu_bli/length(nms))