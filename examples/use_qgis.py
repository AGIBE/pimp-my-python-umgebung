import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
    )

    error_info = (
        "Prüfe die Vorgaben in der README.md, Kapitel "
        "'Nutzung mit QGIS (Bestehende Python Installation)'"
    )

    try:
        import qgis.core

        qgis_version = qgis.core.Qgis.QGIS_VERSION
        logger.info(f"QGIS {qgis_version} is available")
    except ImportError:
        logger.error(f"Import of QGIS failed. {error_info}")

    try:
        import PyQt5

        qt_version = PyQt5.QtCore.QT_VERSION_STR
        logger.info(f"PyQt5 {qt_version} is available")
    except (ImportError, AttributeError):
        logger.error(f"Import of PyQt5 failed. {error_info}")

    try:
        from osgeo import gdal

        gdal_version = gdal.__version__
        logger.info(f"GDAL {gdal_version} is available")
    except ImportError:
        logger.error(f"Import of GDAL from OSGEO failed. {error_info}")

    try:
        from osgeo import ogr

        logger.info(f"OGR is available with {ogr.GetDriverCount()} Drivers")
    except ImportError:
        logger.error(f"Import of OGR from OSGEO failed. {error_info}")


if __name__ == "__main__":
    main()
