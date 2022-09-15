import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    session: ses-[sessionID]
    bids_subject_session_dir: BIDS subject/session directory
    bids_subject_session_prefix: BIDS subject/session prefix
    """

    t1w = create_key('')
    dwi = create_key('')
    loc1_task = create_key('')
    loc2_task = create_key('')
    study1_task = create_key('')
    study2_task = create_key('')
    study3_task = create_key('')
    study4_task = create_key('')
    task_fmap = create_key('')
    dwi_fmap = create_key('')

    info = {t1w : [],
            dwi : [],
            loc1_task : [],
            study1_task : [],
            task_fmap : [],
            dwi_fmap : []}

    for s in seqinfo:
        xdim, ydim, slice_num, timepoints = (s[6], s[7], s[8], s[9])
        if (slice_num == ) and (timepoints == 1) and ("" in s.series_description):
            info[t1w].append(s[2])
        elif (slice_num > 1) and (timepoints == ) and ("" in s[12]):
            info[dwi].append(s[2])
        elif (timepoints == ) and ("" in s[12]):
            info[loc1_task].append(s[2])
        elif (timepoints == ) and ("" in s[12]):
            info[loc2_task].append(s[2])
        elif (timepoints == ) and ('' in s[12]):
            info[study1_task].append(s[2])
        elif "" in s.series_description:
            info[dwi_fmap].append({"item": s[2], "dir": "AP"})
        elif "" in s.series_description:
            info[dwi_fmap].append({"item": s[2], "dir": "PA"})
        elif "" in s.series_description:
            info[task_fmap].append({"item": s[2], "dir": "PA"})
        elif "fMRI_DistortionMap_AP" in s.series_description:
            info[task_fmap].append({"item": s[2], "dir": "AP"})
        else:
            pass
    return info
