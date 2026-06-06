"""
Test for issue #818: COPY TO with certain GDAL drivers crashes

Tests that COPY TO with DRIVER 'MapML' and DRIVER 'GeoRSS' either
succeeds or returns a clear error instead of crashing with
"basic_string: construction from null is not valid".

Regression test for: https://github.com/duckdb/duckdb-spatial/issues/818
"""

import os
import tempfile
import pytest
import duckdb


def test_copy_to_mapml_driver(con):
    """Test COPY TO with MapML driver - should not crash"""
    with tempfile.TemporaryDirectory() as tmp:
        output_path = os.path.join(tmp, "out.mapml")
        sql = f"""
            COPY (SELECT ST_POINT(0.0, 0.0) AS geom)
            TO '{output_path}' (FORMAT GDAL, DRIVER 'MapML')
        """
        # This should either succeed or raise a clear error,
        # but NOT crash with "basic_string: construction from null is not valid"
        con.execute(sql)


def test_copy_to_georss_driver(con):
    """Test COPY TO with GeoRSS driver - should not crash"""
    with tempfile.TemporaryDirectory() as tmp:
        output_path = os.path.join(tmp, "out.georss")
        sql = f"""
            COPY (SELECT ST_POINT(0.0, 0.0) AS geom)
            TO '{output_path}' (FORMAT GDAL, DRIVER 'GeoRSS')
        """
        # This should either succeed or raise a clear error,
        # but NOT crash with "basic_string: construction from null is not valid"
        con.execute(sql)
