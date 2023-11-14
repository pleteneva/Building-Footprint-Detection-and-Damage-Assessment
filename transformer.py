def run_transformer_model(image_path):
    image = load_img(image_path)
    extractor, model = load_model()
    inputs = extractor(images=image, return_tensors="pt").pixel_values
    outputs = model(inputs)
    logits = nn.functional.interpolate(outputs.logits.detach().cpu(),
                                       size=image.size[::-1],
                                       mode='bilinear',
                                       align_corners=False)
    seg = logits.argmax(dim=1)[0].numpy()
    seg = seg.astype(np.uint8)
    polygons, image = mask_to_polygon(np.array(image), seg)
    cv2.imwrite(f"output/{image_path.split('/')[-1]}", image)