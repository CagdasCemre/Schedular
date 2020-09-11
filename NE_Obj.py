class network_element:
    def __init__(self, region=None, branch=None, tech=None, bw=None, target=None, site=None, azimuth=None, isIndoor = None, latitude=None, longitude=None, clusterID = None, occ=None, cleanedSize=None, dayVol=None, dayUtil=None, dayThput=None, bhUtil=None, dayActUE=None, bhThput=None,
                 L800=None, L1800=None, L2100=None, L2600=None, U900=None, U2100=None, G900=None, G1800=None, TOT_BW=None, investmentType = None, recomType=None, rolloutDate=None, updRolloutDate=None, CapEx=None, OpEx=None,
                 comment=None, rolloutCost=None, orig_recomdID=None, recomID=None, purpose=None, radius=None, nearestSiteDistance=None, uson_action_cnt=None, traffic_gain=None, ROI=None, isSkipped=False, corrInfo=None, thput_method=None, b_11=None, b_10=None,
                 skipReason=None, forceToApply=None, coveredPOI=[], mappedRecomType=None, isMatched=False, nearestDistance=None, existingSiteID=None, coveredCnt=0, isClustered=False, isNewSite=0, nearestSiteDist=None,
                 L800_BW=None, L1800_BW=None, L2100_BW=None, L2600_BW=None, priority=None, status=None, source=None, csID=None, causeSite=None, groupID = None):

        self.recomID = recomID
        self.region = region
        self.branch = branch
        self.tech = tech
        self.target = target
        self.isNewSite = isNewSite
        self.site = site
        self.azimuth = azimuth
        self.isIndoor = isIndoor
        self.causeSite = causeSite
        self.latitude = latitude
        self.longitude = longitude
        self.clusterID = clusterID
        self.csID = csID
        self.investmentType = investmentType
        self.recomType = recomType
        self.isSkipped = isSkipped
        self.skipReason = skipReason
        self.forceToApply = forceToApply
        self.groupID = groupID
        self.priority = priority
        self.status = status
        self.source = source
        self.rolloutDate = rolloutDate
        self.CapEx = CapEx
        self.OpEx = OpEx
        self.bw = bw
        self.occ = occ
        self.cleanedSize = cleanedSize
        self.thput_method = thput_method
        self.b_11 = b_11
        self.b_10 = b_10
        self.dayVol = dayVol
        self.bhUtil = bhUtil
        self.dayThput = dayThput
        self.dayUtil = dayUtil
        self.dayActUE = dayActUE
        self.bhThput = bhThput
        self.L800 = L800
        self.L1800 = L1800
        self.L2100 = L2100
        self.L2600 = L2600
        self.U900 = U900
        self.U2100 = U2100
        self.G900 = G900
        self.G1800 = G1800
        self.TOT_BW = TOT_BW
        self.L800_BW = L800_BW
        self.L1800_BW = L1800_BW
        self.L2100_BW = L2100_BW
        self.L2600_BW = L2600_BW
        self.updRolloutDate = updRolloutDate
        self.comment = comment
        self.rolloutCost = rolloutCost
        self.orig_recomdID = orig_recomdID
        self.purpose = purpose
        self.radius = radius
        self.nearestSiteDistance = nearestSiteDistance
        self.uson_action_cnt = uson_action_cnt
        self.traffic_gain = traffic_gain
        self.ROI = ROI
        self.coveredPOI = coveredPOI
        self.mappedRecomType = mappedRecomType
        self.isMatched = isMatched
        self.nearestDistance = nearestDistance
        self.existingSiteID = existingSiteID
        self.coveredCnt = coveredCnt
        self.isClustered = isClustered
        self.nearestSiteDist = nearestSiteDist
        self.corrInfo = corrInfo
