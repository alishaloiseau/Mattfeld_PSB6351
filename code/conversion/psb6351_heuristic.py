from __future__ import annotations
import os

# modify this script 

# heudiconv --files sourcedata/Mattfeld_REVL-000-vCAT-021-S1/scans/*/*/*/*/*.dcm -o raw -f convertall -s 001 -c none --overwrite

# heudiconv --files sourcedata/Mattfeld_REVL-000-vCAT-021-S1/scans/*/*/*/*/*.dcm -o raw -f code/psb6351_heuristic.py -s 001 -ss 01 -c dcm2niix -b


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

    # keyname(e.g.t1w) = create_key('use/this/to/define/sub-{subject}/path/for/file')
    # note you should probably have a key for each scan you want to capture

    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_run-{item:02d}_T1w')

    dwi = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_run-{item:02d}_dwi')

    fmap_func = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-{acquisition}_dir-{direction}_epi') 

    fmap_dwi = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-{acquisition}_dir-{direction}_epi')

    info = {
            t1w: [], 
            dwi: [], 
            fmap_func: [],
            fmap_dwi: [],
           }

    for s in seqinfo:
        xdim, ydim, slice_num, timepoints = (s[6], s[7], s[8], s[9])

        if (slice_num == 176) and (timepoints == 1) and ("T1w_MPR_vNav" in s.series_description)
            info[t1w].append(s[2])
        elif (timepoints == 103) and (timepoints == 1) and ("dMRI_AP_REVL" in s[12]):
            info[dwi].append(s[2])
        
        if (timepoints == 355) and (timepoints == 1) and (
            "fMRI_REVL_Study_2" in s.series_description or
            "fMRI_REVL_Study_3" in s.series_description
            "fMRI_REVL_Study_4" in s.series_description
            )
            info[fmap_func].append(s[2], "direction", "acquistion")
    
        '''else:
            pass'''
    return info
